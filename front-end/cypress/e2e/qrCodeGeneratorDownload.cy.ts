/// <reference types="cypress" />

describe('QR Code Generator Download', () => {
  
  it('should download the QR code', () => {
    cy.intercept('POST', '/qrcode').as('qrCodeGenerator');

    cy.visit('/');

    cy.get('#link').type('https://example.com');
    
    cy.get('#formQRCode').submit();

    cy.get('#qrcode').should('be.visible');
    cy.get('#qrcode').should('have.attr', 'src').and('include', 'data:image/png;base64,');

    cy.get('.download-share-buttons button').contains('Download').click();
  });
});
