import { useContext } from "react";
import { Carousel, v } from "../../index";
import { ThemeContext } from "../../App";

function ExternalLinkButton({ url, titulo, bgcolor, Icon }) {
  return (
    <a
      href={url}
      target="_blank"
      rel="noreferrer"
      className="z-[2] flex items-center gap-2.5 no-underline"
    >
      <span className="text-xl">
        <Icon />
      </span>
      <span
        className="cursor-pointer rounded-[0.4em] border-[3px] border-black px-[1.3em] py-[0.6em] text-lg font-black text-black shadow-[0.1em_0.1em_#000] transition duration-200 hover:-translate-x-[0.05em] hover:-translate-y-[0.05em] hover:shadow-[0.15em_0.15em_#000] active:translate-x-[0.05em] active:translate-y-[0.05em] active:shadow-[0.05em_0.05em_#000]"
        style={{ background: bgcolor }}
      >
        {titulo}
      </span>
    </a>
  );
}

export function HomeTemplate() {
  const { theme } = useContext(ThemeContext);
  const isLight = theme === "light";

  return (
    <main
      className={`relative flex min-h-screen w-full items-center justify-center overflow-hidden ${
        isLight ? "bg-[#EDF3FB]" : "bg-[#1C1C1E]"
      }`}
    >
      <div className="mx-auto flex w-3/4 flex-col items-center justify-center text-center">
        <div className="flex min-h-[60vh] w-1/2 flex-col items-center justify-center max-sm:min-h-[50vh]">
          <Carousel />
        </div>

        <h2
          className={`mx-auto w-4/5 self-start text-left text-[3em] capitalize max-lg:w-full max-lg:text-center max-sm:text-[2em] max-[30em]:text-[1.25em] ${
            isLight ? "text-[#202020]" : "text-white"
          }`}
        >
          Bienvenido a Cerdyn <br /> 🐷
        </h2>

        <p className="mx-auto my-4 w-4/5 self-start text-left text-[1.25em] font-normal text-[#8e8c86] max-lg:w-full max-lg:text-center max-lg:text-base max-sm:text-base max-[30em]:text-sm">
          Cerdyn nace por las pocas aplicaciones gratis que existen para
          controlar gastos e ingresos.
          <br />
          ❤️Está surgiendo como curso para lograr presupuestarlo,
          <br /> MUCHAS GRACIAS POR APOYAR ESTE PROYECTO
        </p>

        <div className="flex items-center gap-5">
          <div className="h-20 w-20 overflow-hidden rounded-full">
            <img
              src="https://i.ibb.co/6Nw0B9p/yjtityutyu.png"
              alt="Ing. Franklin Bustamante"
              className="h-full w-full object-contain"
            />
          </div>
          <div className="flex flex-col text-left">
            <b className={isLight ? "text-[#202020]" : "text-white"}>
              Ing. Franklin Bustamante
            </b>
            <span className="text-[#8c8c8c]">&quot;cualquiera puede programar&quot;</span>
          </div>
        </div>

        <div className="mx-auto my-4 flex w-4/5 flex-wrap justify-center gap-5 self-center max-lg:w-full">
          <ExternalLinkButton
            url="https://t.me/htmlycss369"
            titulo="UNIRSE A Telegram"
            bgcolor="#BF94FF"
            Icon={v.iconoreact}
          />
          <ExternalLinkButton
            url="https://www.udemy.com/course/sistema-para-el-control-de-gastos-con-reactjs-y-postgresql/?couponCode=CERDYNREACT"
            titulo="Ver curso"
            bgcolor="#fb37b7"
            Icon={v.iconocorona}
          />
        </div>
      </div>
    </main>
  );
}
