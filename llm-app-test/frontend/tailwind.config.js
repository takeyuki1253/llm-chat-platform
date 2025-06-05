/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#e6f1ff',
          100: '#b3d4ff',
          200: '#80b7ff',
          300: '#4d9aff',
          400: '#1a7dff',
          500: '#0066e6',
          600: '#0051b3',
          700: '#003d80',
          800: '#00294d',
          900: '#00141a',
        },
        secondary: {
          50: '#f3e5ff',
          100: '#d9b3ff',
          200: '#bf80ff',
          300: '#a64dff',
          400: '#8c1aff',
          500: '#7300e6',
          600: '#5900b3',
          700: '#400080',
          800: '#26004d',
          900: '#0d001a',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['Fira Code', 'monospace'],
      },
    },
  },
  plugins: [],
}