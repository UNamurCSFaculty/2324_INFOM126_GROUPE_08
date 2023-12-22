/// <reference types="cypress" />

describe('GuestBook List', () => {

  it('Displays guest book entries and check "User" and "This is a test message" ', () => {
    cy.intercept('GET', '/guest-book').as('formSubmission');
    cy.visit('/');

    cy.wait(1000);

    cy.get('.table-container table tbody tr').should('have.length.gte', 1);

    cy.get('.table-container table tbody tr:first-child td').should('have.length', 3);

    cy.get('.table-container table tbody tr:first-child td:first-child').should('contain.text', 'User');
    cy.get('.table-container table tbody tr:first-child td:nth-child(2)').should('contain.text', 'This is a test message.');
  });
});

