import { Reveal } from "@/components/ui/Reveal";
import { SectionTitle } from "@/components/ui/SectionTitle";

export function Experience() {
  return (
    <section
      id="experiencia"
      className="border-t border-panem-gold/10 px-6 py-24 md:py-32"
    >
      <div className="mx-auto max-w-7xl">
        <Reveal>
          <SectionTitle
            eyebrow="03 / Trayectoria"
            title="Experiencia"
            description="Una línea temporal de experiencias académicas, actividades y aprendizajes relevantes."
          />
        </Reveal>

        <div className="space-y-8">
          <Reveal delay={0.1}>
            <article className="grid gap-4 border-l border-panem-gold/30 pl-6 md:grid-cols-[180px_1fr]">
              <p className="text-sm uppercase tracking-[0.2em] text-panem-gold">
                2026
              </p>

              <div>
                <h3 className="text-xl font-semibold">
                  Experiencia académica
                </h3>

                <p className="mt-3 leading-8 text-panem-ivory/60">
                  Aquí colocaremos una experiencia real de tu trayectoria
                  académica.
                </p>
              </div>
            </article>
          </Reveal>
        </div>
      </div>
    </section>
  );
}