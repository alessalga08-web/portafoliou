import { Reveal } from "@/components/ui/Reveal";
import { SectionTitle } from "@/components/ui/SectionTitle";

const technicalSkills = [
  "Programación",
  "Manejo de Microsoft Excel a nivel avanzado",
  "Dominio de un segundo idioma(Nivel Intermedio)",
  "Pensamiento matemático",
];

const personalSkills = [
  "Trabajo en equipo",
  "Facilidad de aprendizaje y adaptación",
  "Creatividad",
  "Resolución de problemas",
];

export function Skills() {
  return (
    <section
      id="habilidades"
      className="border-t border-panem-gold/10 px-6 py-24 md:py-32"
    >
      <div className="mx-auto max-w-7xl">
        <Reveal>
          <SectionTitle
            eyebrow="05 / Capacidades"
            title="Habilidades"
            description="Conocimientos técnicos y habilidades personales desarrolladas durante mi formación."
          />
        </Reveal>

        <div className="grid gap-8 md:grid-cols-2">
          <Reveal delay={0.1}>
            <div className="border border-panem-gold/20 p-8">
              <h3 className="text-xl font-semibold text-panem-gold">
                Técnicas
              </h3>

              <ul className="mt-6 space-y-4">
                {technicalSkills.map((skill) => (
                  <li
                    key={skill}
                    className="border-b border-panem-gold/10 pb-3 text-panem-ivory/70"
                  >
                    {skill}
                  </li>
                ))}
              </ul>
            </div>
          </Reveal>

          <Reveal delay={0.2}>
            <div className="border border-panem-gold/20 p-8">
              <h3 className="text-xl font-semibold text-panem-gold">
                Personales
              </h3>

              <ul className="mt-6 space-y-4">
                {personalSkills.map((skill) => (
                  <li
                    key={skill}
                    className="border-b border-panem-gold/10 pb-3 text-panem-ivory/70"
                  >
                    {skill}
                  </li>
                ))}
              </ul>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}