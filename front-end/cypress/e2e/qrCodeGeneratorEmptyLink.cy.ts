/// <reference types="cypress" />

describe('QR Code Generator Empty Link', () => {

  it('displays an error message for empty link in QR code generator', () => {
    cy.intercept('POST', '/qrcode').as('qrCodeGenerator');

    cy.visit('/');

    cy.get('#formQRCode').submit();

    cy.get('.qr-code-error-message').should('be.visible').and('contain.text', 'Please enter a valid link.');

    cy.get('#qrcode').should('not.exist');
  });
});
