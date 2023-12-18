// cypress/integration/qrcodeGenerator.spec.ts
/// <reference types="cypress" />

describe('QR Code Generator Tests', () => {
  it('should generate a QR code', () => {
    cy.visit('/');
  
    cy.get('#url').type('https://example.com');
    cy.get('form').submit();
    cy.get('#qrcode img').should('be.visible');
    cy.get('#qrcode img').should('have.attr', 'src').and('include', 'data:image/png;base64,');
  });
});
  
