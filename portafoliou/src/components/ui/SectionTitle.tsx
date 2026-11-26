interface SectionTitleProps {
  eyebrow: string;
  title: string;
  description?: string;
}

export function SectionTitle({
  eyebrow,
  title,
  description,
}: SectionTitleProps) {
  return (
    <div className="mb-12 max-w-3xl">
      <p className="mb-3 text-sm uppercase tracking-[0.3em] text-panem-gold">
        {eyebrow}
      </p>

      <h2 className="text-3xl font-bold tracking-tight md:text-5xl">
        {title}
      </h2>

      {description && (
        <p className="mt-5 leading-8 text-panem-ivory/60">
          {description}
        </p>
      )}
    </div>
  );
}