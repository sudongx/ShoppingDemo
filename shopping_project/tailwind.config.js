// tailwind.config.js
module.exports = {
    content: [
        "./**/*.html",  // 扫描所有模板文件
    ],
    theme: {
        extend: {
            colors: {
                primary: '#165DFF',
                secondary: '#FF7D00',
                neutral: {
                    100: '#F5F7FA',
                    200: '#E5E6EB',
                    300: '#C9CDD4',
                    400: '#86909C',
                    500: '#4E5969',
                    600: '#1D2129',
                }
            },
            fontFamily: {
                inter: ['Inter', 'sans-serif'],
            },
            fontSize: {
                'xs': '1rem',
                'sm': '1.125rem',
                'base': '1.25rem',
                'lg': '1.5rem',
                'xl': '1.75rem',
                '2xl': '2rem',
                '3xl': '2.25rem',
                '4xl': '2.5rem',
                '5xl': '3rem',
                '6xl': '3.75rem',
                '7xl': '4.5rem',
                '8xl': '6rem',
                '9xl': '8rem'
            },
            spacing: {
                'px': '1px',
                '0': '0px',
                '0.5': '0.125rem',
                '1': '0.25rem',
                '1.5': '0.375rem',
                '2': '0.5rem',
                '2.5': '0.625rem',
                '3': '0.75rem',
                '3.5': '0.875rem',
                '4': '1rem',
                '5': '1.25rem',
                '6': '1.5rem',
                '7': '1.75rem',
                '8': '2rem',
                '9': '2.25rem',
                '10': '2.5rem',
                '11': '2.75rem',
                '12': '3rem',
                '14': '3.5rem',
                '16': '4rem',
                '20': '5rem',
                '24': '6rem',
                '28': '7rem',
                '32': '8rem',
                '36': '9rem',
                '40': '10rem',
                '44': '11rem',
                '48': '12rem',
                '52': '13rem',
                '56': '14rem',
                '60': '15rem',
                '64': '16rem',
                '72': '18rem',
                '80': '20rem',
                '96': '24rem'
            }
        },
    },
    plugins: [],
}