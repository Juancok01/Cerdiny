import { create } from "zustand";
import { supabase } from "../index";

export const useAuthStore = create((set) => ({
  isAuth: false,
  datauserGoogle: [],
  signInWithGoogle: async () => {
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider: "google",
    });
    if (error) throw error;
    set({ isAuth: true });
    return data;
  },
  signInWithApple: async () => {
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider: "apple",
    });
    if (error) throw error;
    return data;
  },
  signInWithEmail: async ({ email, password }) => {
    const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password,
    });
    if (error) throw error;
    set({ isAuth: true });
    return data;
  },
  signUpWithEmail: async ({ email, password }) => {
    const { data, error } = await supabase.auth.signUp({
      email,
      password,
    });
    if (error) throw error;
    return data;
  },
  resetPassword: async (email) => {
    const { error } = await supabase.auth.resetPasswordForEmail(
      email.trim().toLowerCase(),
      {
        redirectTo: window.location.href.split("#")[0],
      }
    );
    if (error) throw error;
  },
  signout: async () => {
    const { error } = await supabase.auth.signOut();
    set({ isAuth: false });
    if (error) throw new Error("A ocurrido un error durante el cierre de sesión");
  },
}));
