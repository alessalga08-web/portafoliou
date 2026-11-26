export interface Project {
  id: string;
  title: string;
  description: string;
  objective: string;
  problem: string;
  technologies: string[];
  procedure: string[];
  results: string[];
  screenshots: string[];
  repository?: string;
  featured?: boolean;
}

export interface Skill {
  name: string;
  category: "technical" | "personal";
  level?: string;
}

export interface Education {
  institution: string;
  degree: string;
  period: string;
  description?: string;
}