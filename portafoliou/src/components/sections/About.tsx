import { Reveal } from "@/components/ui/Reveal";
import { SectionTitle } from "@/components/ui/SectionTitle";

export function About() {
  return (
    <section
      id="sobre-mi"
      className="border-t border-panem-gold/10 px-6 py-24 md:py-32"
    >
      <div className="mx-auto max-w-7xl">
        <Reveal>
          <SectionTitle
            eyebrow="02 / Expediente"
            title="Sobre mí"
          />
        </Reveal>

        <div className="grid gap-8 md:grid-cols-2">
          <Reveal delay={0.1}>
            <div className="border border-panem-gold/20 bg-panem-ivory/[0.03] p-8">
              <p className="mb-4 text-sm uppercase tracking-[0.2em] text-panem-gold">
                Perfil
              </p>

              <p className="leading-8 text-panem-ivory/70">
                Soy una persona curiosa, amable, íntegra y resiliente.
                Me gusta buscar diferentes formas de hacer las cosas,
                aprender constantemente y enfrentar cada reto como
                una oportunidad para mejorar y adquirir nuevos conocimientos.
              </p>
            </div>
          </Reveal>

          <Reveal delay={0.2}>
            <div className="border border-panem-gold/20 bg-panem-ivory/[0.03] p-8">
              <p className="mb-4 text-sm uppercase tracking-[0.2em] text-panem-gold">
                Lo que me define
              </p>

              <p className="leading-8 text-panem-ivory/70">
                Me define mi curiosidad, mi disposición para aprender 
                y mi perseverancia. Busco siempre mejorar, encontrar 
                nuevas soluciones y crecer a través de cada experiencia.
              </p>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}