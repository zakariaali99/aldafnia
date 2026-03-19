/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    darkMode: 'class',
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        '../../static/**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        '../../**/views.py',
        '../../**/forms.py',
    ],
    theme: {
        extend: {
            colors: {
                primary: {
                    DEFAULT: '#0054a6',
                    dark: '#3b82f6',
                },
                secondary: {
                    DEFAULT: '#00aee6',
                    dark: '#06b6d4',
                },
                surface: {
                    DEFAULT: '#ffffff',
                    dark: '#1e293b',
                },
                background: {
                    DEFAULT: '#f8f9fa',
                    dark: '#0f172a',
                },
                text: {
                    DEFAULT: '#1a202c',
                    dark: '#e2e8f0',
                },
            },
            fontFamily: {
                cairo: ['Cairo', 'sans-serif'],
                almarai: ['Almarai', 'sans-serif'],
                inter: ['Inter', 'sans-serif'],
                roboto: ['Roboto', 'sans-serif'],
            },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
