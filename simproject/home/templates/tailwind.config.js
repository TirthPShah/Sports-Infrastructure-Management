/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["*"],
    theme: {
      extend: {
        lineHeight: {
          '110': '110px',
        },
        width: {
          '156': '156px',
        },
      },
    },
    plugins: [
      function ({ addUtilities }) {
        const newUtilities = {
          '.scrollbar-hide': {
            /* Hide scrollbar for Webkit browsers */
            '::-webkit-scrollbar': {
              display: 'none',
            },
            /* Hide scrollbar for other browsers */
            '-ms-overflow-style': 'none', /* IE and Edge */
            'scrollbar-width': 'none', /* Firefox */
          },
          '.scrollbar-custom': {
            /* Customize scrollbar track */
            '::-webkit-scrollbar': {
              width: '12px',
            },
            '::-webkit-scrollbar-track': {
              background: '#f1f1f1',
            },
            '::-webkit-scrollbar-thumb': {
              background: '#888',
              borderRadius: '10px',
            },
            '::-webkit-scrollbar-thumb:hover': {
              background: '#555',
            },
          },
        };
        addUtilities(newUtilities, ['responsive', 'hover']);
      },
    ],
  };
  