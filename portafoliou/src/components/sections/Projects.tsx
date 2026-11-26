import { Reveal } from "@/components/ui/Reveal";
import { SectionTitle } from "@/components/ui/SectionTitle";

const githubUrl =
  "https://github.com/alessalga08-web/portafoliou";

const projectNames = [
  {
    number: "01",
    title: "Regresión lineal",
    description:
      "Proyecto académico de análisis y modelado mediante regresión lineal.",
    path: "/tree/main/projects/regresion-lineal",
  },
  {
    number: "02",
    title: "Laberinto",
    description:
      "Juego desarrollado con Python y Pygame utilizando generación procedural de laberintos.",
    path: "/tree/main/projects/laberinto",
  },
  {
    number: "03",
    title: "AI Challenge",
    description:
      "Proyecto académico de inteligencia artificial que trabaja con K-Means y KNN.",
    path: "/tree/main/projects/ai-challenge",
  },
  {
    number: "04",
    title: "Hotspots Comerciales",
    description:
      "Proyecto académico de análisis geográfico utilizando K-Means, KNN y mapas interactivos.",
    path: "/tree/main/projects/hotspots-comerciales",
  },
];

export function Projects() {
  return (
    <section
      id="proyectos"
      className="border-t border-panem-gold/10 px-6 py-24 md:py-32"
    >
      <div className="mx-auto max-w-7xl">
        <Reveal>
          <SectionTitle
            eyebrow="04 / Proyectos"
            title="Proyectos académicos"
            description="Una colección de proyectos desarrollados durante mi proceso de formación."
          />
        </Reveal>

        <div className="grid gap-6 md:grid-cols-2">
          {projectNames.map((project, index) => (
            <Reveal
              key={project.number}
              delay={index * 0.1}
            >
              <article className="group h-full border border-panem-gold/20 bg-panem-ivory/[0.03] p-8 transition duration-300 hover:border-panem-gold/60 hover:bg-panem-red/10">
                <p className="text-sm text-panem-gold">
                  {project.number}
                </p>

                <h3 className="mt-6 text-2xl font-semibold">
                  {project.title}
                </h3>

                <p className="mt-4 leading-7 text-panem-ivory/60">
                  {project.description}
                </p>

                <div className="mt-8 h-px w-12 bg-panem-gold transition-all duration-300 group-hover:w-24" />

                <a
                  href={`${githubUrl}${project.path}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="mt-8 inline-block border border-panem-gold/40 px-4 py-2 text-sm font-medium text-panem-gold transition hover:bg-panem-gold hover:text-panem-black"
                >
                  VER CÓDIGO EN GITHUB
                </a>
              </article>
            </Reveal>
          ))}
        </div>

        <Reveal delay={0.4}>
          <div className="mt-12 flex justify-center">
            <a
              href={githubUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="border border-panem-gold bg-panem-gold px-6 py-3 font-semibold text-panem-black transition hover:bg-transparent hover:text-panem-gold"
            >
              VER MI GITHUB
            </a>
          </div>
        </Reveal>
      </div>
    </section>
  );
}