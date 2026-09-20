import { createContext, useContext, useEffect, useState } from "react";
import { supabase,InsertarUsuarios } from "../index";
const AuthContext = createContext();
export const AuthContextProvider = ({ children }) => {
  const [user, setUser] = useState([]);
  useEffect(() => {
    const { data: authListener } = supabase.auth.onAuthStateChange(
      async (event, session) => {
        if (session == null) {
          setUser(null);
        } else {
          setUser(session?.user.user_metadata);
          insertarUsuarios(
            session?.user.user_metadata,
            session?.user.id,
            session?.user.email
          );
          // console.log("event", event);
          // console.log("session", session?.user.user_metadata);
        }
      }
    );
    return () => {
      authListener.subscription;
    };
  }, []);
  const insertarUsuarios = async (dataProvider, idAuthSupabase, email) => {
    const p = {
      nombres:
        dataProvider?.name ||
        dataProvider?.full_name ||
        email?.split("@")[0] ||
        "Usuario",
      foto: dataProvider?.picture || dataProvider?.avatar_url || "",
      idauth_supabase: idAuthSupabase,
    };
    await InsertarUsuarios(p);
  };
  return (
    <AuthContext.Provider value={{ user }}>{children}</AuthContext.Provider>
  );
};
export const UserAuth = () => {
  return useContext(AuthContext);
};
