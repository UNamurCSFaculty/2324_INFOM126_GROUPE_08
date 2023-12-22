/// <reference types="cypress" />

describe('GuestBook Form', () => {

  it('submits the form with invalid name and expects failure', () => {
    cy.intercept('POST', '/guest-book').as('formSubmission');

    cy.visit('/');

    cy.get('#nom').clear();
    cy.get('#message').type('MessageError');

    cy.get('#formGuestBook').submit();

    cy.get('.error-message').should('be.visible').and('contain.text', 'Name and message are required.');

    cy.get('.response-message').should('not.contain.text', 'New message successfully saved !');
  });
});
