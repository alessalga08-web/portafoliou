"use client";

import { FormEvent, useState } from "react";
import { Reveal } from "@/components/ui/Reveal";
import { SectionTitle } from "@/components/ui/SectionTitle";

export function Contact() {
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("");

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    setLoading(true);
    setStatus("");

    const form = event.currentTarget;
    const formData = new FormData(form);

    const data = {
      name: formData.get("name"),
      email: formData.get("email"),
      message: formData.get("message"),
    };

    try {
      const response = await fetch("/api/contact", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();

      if (!response.ok) {
        throw new Error(result.message);
      }

      setStatus("Mensaje enviado correctamente.");
      form.reset();
    } catch {
      setStatus("No fue posible enviar el mensaje.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <section
      id="contacto"
      className="border-t border-panem-gold/10 px-6 py-24 md:py-32"
    >
      <div className="mx-auto max-w-7xl">
        <Reveal>
          <SectionTitle
            eyebrow="07 / Comunicación"
            title="Contacto"
            description="Si deseas comunicarte conmigo, puedes utilizar el siguiente formulario."
          />
        </Reveal>

        <Reveal delay={0.1}>
          <form
            onSubmit={handleSubmit}
            className="max-w-2xl space-y-6"
          >
            <div>
              <label
                htmlFor="name"
                className="mb-2 block text-sm text-panem-ivory/70"
              >
                Nombre completo
              </label>

              <input
                id="name"
                name="name"
                type="text"
                required
                className="w-full border border-panem-gold/20 bg-panem-ivory/[0.03] px-4 py-3 outline-none transition focus:border-panem-gold"
              />
            </div>

            <div>
              <label
                htmlFor="email"
                className="mb-2 block text-sm text-panem-ivory/70"
              >
                Correo electrónico
              </label>

              <input
                id="email"
                name="email"
                type="email"
                required
                className="w-full border border-panem-gold/20 bg-panem-ivory/[0.03] px-4 py-3 outline-none transition focus:border-panem-gold"
              />
            </div>

            <div>
              <label
                htmlFor="message"
                className="mb-2 block text-sm text-panem-ivory/70"
              >
                Mensaje
              </label>

              <textarea
                id="message"
                name="message"
                rows={6}
                required
                className="w-full resize-none border border-panem-gold/20 bg-panem-ivory/[0.03] px-4 py-3 outline-none transition focus:border-panem-gold"
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className="border border-panem-gold bg-panem-gold px-6 py-3 font-semibold text-panem-black transition hover:bg-transparent hover:text-panem-gold disabled:cursor-not-allowed disabled:opacity-50"
            >
              {loading ? "ENVIANDO..." : "ENVIAR MENSAJE"}
            </button>

            {status && (
              <p className="text-sm text-panem-gold">
                {status}
              </p>
            )}
          </form>
        </Reveal>
      </div>
    </section>
  );
}