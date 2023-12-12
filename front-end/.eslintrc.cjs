module.exports = {
    "root": true,
    "parser": "vue-eslint-parser",
    "parserOptions": {
        "parser": "@typescript-eslint/parser",
    },
    "extends": [
        "plugin:vue/recommended",
        "eslint:recommended"
    ],
    "plugins": ["@typescript-eslint"],
    "rules": {
        "vue/first-attribute-linebreak": ["error", {
            "singleline": "ignore",
            "multiline": "ignore"
        }],
        "vue/max-attributes-per-line": ["error", {
            "singleline": {
                "max": 8
            },
            "multiline": {
                "max": 8
            }
        }],
        "vue/html-closing-bracket-newline": 'off',
        'vue/singleline-html-element-content-newline': 'off',
        'vue/multiline-html-element-content-newline': 'off',
        'vue/html-self-closing': 'off',
        'vue/no-multiple-template-root': 'off'
    }
}