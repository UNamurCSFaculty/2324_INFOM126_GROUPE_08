// cypress/integration/qrcodeGenerator.spec.ts
/// <reference types="cypress" />

describe('QR Code Generator Tests', () => {
  it('should generate a QR code', () => {
    cy.visit('/');
  
    cy.get('#link').type('https://example.com');
    cy.get('#formQRCode').submit();

    cy.get('#qrcode').should('be.visible');
    cy.get('#qrcode').should('have.attr', 'src').and('include', 'data:image/png;base64,');
  });
});
  
