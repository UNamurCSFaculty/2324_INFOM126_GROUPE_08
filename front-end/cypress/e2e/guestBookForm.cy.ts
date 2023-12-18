/// <reference types="cypress" />

describe('GuestBook Form', () => {
    beforeEach(() => {
      cy.visit('/');
    });
  
    it('submits the form with valid data', () => {
      cy.get('#nom').type('Maxou');
      cy.get('#message').type('This is a test message.');
  
      cy.get('#formGuestBook').submit();
  
      cy.wait(1000); 
  
      cy.get('.success-message').should('contain.text', 'Entry successfully added');
    });
  });
  
