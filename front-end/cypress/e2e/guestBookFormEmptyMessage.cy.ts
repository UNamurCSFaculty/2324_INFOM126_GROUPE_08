/// <reference types="cypress" />

describe('GuestBook Form', () => {

  it('submits the form with invalid message and expects failure', () => {
    cy.intercept('POST', '/guest-book').as('formSubmission');

    cy.visit('/');

    cy.get('#nom').type('UserError');

    cy.get('#message').clear();

    cy.get('#formGuestBook').submit();

    cy.get('.error-message').should('be.visible').and('contain.text', 'Name and message are required.');

    cy.get('.response-message').should('not.contain.text', 'New message successfully saved !');
  });
});
