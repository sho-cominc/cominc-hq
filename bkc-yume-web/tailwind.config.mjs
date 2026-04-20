/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        ink: '#0B0B0C',
        cream: '#FFF8EE',
        berry: '#FF6F8E',
        caramel: '#D8A15A',
        sub: '#8A8A8D',
        line: '#1F1F22',
      },
      fontFamily: {
        display: ['"Bagel Fat One"', 'system-ui', 'sans-serif'],
        jp: ['"Zen Maru Gothic"', '"Hiragino Maru Gothic ProN"', 'sans-serif'],
        en: ['"DM Sans"', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        blob: '28px',
      },
    },
  },
  plugins: [],
};
