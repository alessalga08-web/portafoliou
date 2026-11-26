
import Image from "next/image";

import { Navbar } from "@/components/layout/Navbar";
import { About } from "@/components/sections/About";
import { Contact } from "@/components/sections/Contact";
import { Education } from "@/components/sections/Education";
import { Experience } from "@/components/sections/Experience";
import { Projects } from "@/components/sections/Projects";
import { Skills } from "@/components/sections/Skills";

export default function Home() {
  return (
    <main className="min-h-screen bg-panem-black text-panem-ivory">
      <Navbar />

      {/* INICIO */}
      <section
        id="inicio"
        className="flex min-h-screen items-center px-6 pt-24"
      >
        <div className="mx-auto grid max-w-7xl items-center gap-12 md:grid-cols-2">

          {/* Texto */}
          <div className="text-center md:text-left">
            <p className="mb-4 text-sm uppercase tracking-[0.4em] text-panem-gold">
              Expediente personal
            </p>

            <h1 className="text-5xl font-bold tracking-tight md:text-7xl">
              PORTAFOLIO
            </h1>

            <div className="my-8 mx-auto h-px w-24 bg-panem-gold md:mx-0" />

            <h2 className="text-2xl font-semibold md:text-3xl">
              Enrique Alejandro Salgado Menjívar
            </h2>

            <p className="mx-auto mt-6 max-w-2xl text-lg leading-relaxed text-panem-ivory/70 md:mx-0">
              Una colección de experiencias, proyectos académicos,
              conocimientos y objetivos profesionales.
            </p>

            <a
              href="#proyectos"
              className="mt-8 inline-block border border-panem-gold px-6 py-3 text-sm font-semibold uppercase tracking-wider text-panem-gold transition hover:bg-panem-gold hover:text-panem-black"
            >
              Ver proyectos
            </a>
          </div>

          {/* Foto */}
          <div className="flex justify-center md:justify-end">
            <div className="relative">

              {/* Marco decorativo */}
              <div className="absolute -inset-3 border border-panem-gold/30" />
              <div className="absolute -inset-6 border border-panem-gold/10" />

              {/* Foto de perfil */}
              <div className="relative h-80 w-64 overflow-hidden border border-panem-gold/50 bg-panem-ivory/[0.03] md:h-[430px] md:w-[340px]">
                <Image
                  src="/foto-perfil.png"
                  alt="Fotografía personal"
                  fill
                  priority
                  sizes="(max-width: 768px) 256px, 340px"
                  className="object-cover"
                />
              </div>

              {/* Etiqueta */}
              <div className="absolute -bottom-5 -left-5 border border-panem-gold/40 bg-panem-black px-5 py-3">
                <p className="text-xs uppercase tracking-[0.25em] text-panem-gold">
                  Expediente
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* SOBRE MÍ */}
      <About />

      {/* EXPERIENCIA */}
      <Experience />

      {/* PROYECTOS */}
      <Projects />

      {/* HABILIDADES */}
      <Skills />

      {/* EDUCACIÓN */}
      <Education />

      {/* CONTACTO */}
      <Contact />
    </main>
  );
}
