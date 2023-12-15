/// <reference types="cypress" />

describe('Guest Book Component', () => {
    beforeEach(() => {
      cy.visit('/');
    });
  
    it('fetches and displays guest book entries', () => {
    
      cy.wait(1000);

      cy.get('.table-container table tbody tr').should('have.length.gte', 1);
  
      cy.get('.table-container table tbody tr:first-child td').should('have.length', 3);

      cy.get('.table-container table tbody tr:first-child td:first-child').should('contain.text', 'Maxou');
      cy.get('.table-container table tbody tr:first-child td:nth-child(2)').should('contain.text', 'This is a test message.');
     
    });
  });
  