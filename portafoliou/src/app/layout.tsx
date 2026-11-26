import type { Metadata } from "next";
// @ts-ignore Next.js handles global CSS imports at build time.
import "./globals.css";

export const metadata: Metadata = {
  title: "Portafolio | Panem",
  description:
    "Portafolio digital personal inspirado en la estética de Panem.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  );
}