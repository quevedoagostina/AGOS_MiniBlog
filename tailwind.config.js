/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["C:/Users/Agos/Documents/PYTHONBLOG/templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [
    // ...
    require('@tailwindcss/forms'),
  ],
}

