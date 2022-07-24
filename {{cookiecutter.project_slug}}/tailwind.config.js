module.exports = {
  mode: "jit",
  purge: [
    "./application/templates/**/*.html",
    "./application//home/templates/**/*.html",
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter var", "sans-serif"],
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
