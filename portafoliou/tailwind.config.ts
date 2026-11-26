import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        panem: {
          black: "#171717",
          red: "#751F27",
          gold: "#C6A45C",
          ivory: "#E9E1D2",
        },
      },
    },
  },
  plugins: [],
};

export default config;