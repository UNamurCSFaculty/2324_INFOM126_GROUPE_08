/// <reference types="cypress" />

describe('GuestBook Form', () => {

  it('submits the form with valid data', () => {
    cy.intercept('POST', '/guest-book').as('formSubmission');

    cy.visit('/');

    cy.get('#nom').type('User');
    cy.get('#message').type('This is a test message.');

    cy.get('#formGuestBook').submit();

    cy.wait('@formSubmission')
      .its('response.body.message')
      .should('contain', 'New message successfully saved !');

    cy.get('.response-message').should('contain.text', 'New message successfully saved !');
  });
});

