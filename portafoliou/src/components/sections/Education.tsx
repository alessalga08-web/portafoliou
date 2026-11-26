import { Reveal } from "@/components/ui/Reveal";
import { SectionTitle } from "@/components/ui/SectionTitle";

export function Education() {
  return (
    <section
      id="educacion"
      className="border-t border-panem-gold/10 px-6 py-24 md:py-32"
    >
      <div className="mx-auto max-w-7xl">
        <Reveal>
          <SectionTitle
            eyebrow="06 / Formación"
            title="Educación"
            description="Formación académica, cursos y conocimientos adquiridos."
          />
        </Reveal>

        <Reveal delay={0.1}>
          <article className="border border-panem-gold/20 p-8">
            <p className="text-sm uppercase tracking-[0.2em] text-panem-gold">
              Formación académica
            </p>

            <h3 className="mt-4 text-2xl font-semibold">
              BACHILLERATO GENERAL
            </h3>

            <p className="mt-4 leading-8 text-panem-ivory/60">
              Complejo Educativo Católico “Fray Martín de Porres”
              <br></br>
              2025-2026
            </p>
            <br></br>

            <h3 className="mt-4 text-2xl font-semibold">
              DIPLOMADO
            </h3>
            <p className="mt-4 leading-8 text-panem-ivory/60">
              PROGRAMA EMPRESARIAL ¡SUPÉRATE! FUNDACIÓN FRECH
              <br></br>
              Diplomado en Valores, Inglés e Informática
              <br></br>
              2024-2026
            </p>

             <h3 className="mt-4 text-2xl font-semibold">
              CERTIFICACIONES
            </h3>
            <p className="mt-4 leading-8 text-panem-ivory/60">
              Most Excel Expert 
              <br></br>
              TOEIC Speaking and Writing
              <br></br>
              TOEIC Listening and Reading
            </p>
          </article>
        </Reveal>
      </div>
    </section>
  );
}