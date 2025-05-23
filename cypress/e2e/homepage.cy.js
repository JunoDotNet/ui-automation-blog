describe('Homepage UI Test', () => {
  it('loads and displays categories', () => {
    cy.visit('/');

    cy.get('button')
      .should('exist')
      .and('have.length.at.least', 1);

    cy.contains('Tutorials').should('be.visible'); 
  });
});
