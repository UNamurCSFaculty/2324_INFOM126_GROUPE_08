/// <reference types="cypress" />

describe('QR Code Generator Invalid Link', () => {

  it('displays an error message for invalid link in QR code generator', () => {
    cy.intercept('POST', '/qrcode').as('qrCodeGenerator');

    cy.visit('/');

    cy.get('#link').type('invalid-link');

    cy.get('#formQRCode').submit();

    cy.get('.qr-code-error-message').should('be.visible').and('contain.text', 'Please enter a valid link.');

    cy.get('#qrcode').should('not.exist');
  });
});
