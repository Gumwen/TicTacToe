# Tic-Tac-Toe Game

Tic Tac Toe is a simple two-player game played on a 3x3 grid. Players take turns marking a square with either X or O, trying to align three of their marks in a row, column, or diagonal.

---

## Propositional Logic

The game mechanics are defined using propositions that represent each cell of the 3x3 TicTacToe grid:

### Propositions

- \( H(i, j) \): The human has marked cell \((i, j)\).
- \( C(i, j) \): The computer has marked cell \((i, j)\).
- \( E(i, j) \): The cell \((i, j)\) is empty.
- \( W_H \): The human wins.
- \( W_C \): The computer wins.
- \( D \): The game ends in a draw.

### Winning Conditions

#### Rows

A player wins if all cells in a row are marked by the same player:

- **For the Human**:  
  \( \forall i \, (H(i, 0) \land H(i, 1) \land H(i, 2)) \to W_H \)

- **For the Computer**:  
  \( \forall i \, (C(i, 0) \land C(i, 1) \land C(i, 2)) \to W_C \)

#### Columns

A player wins if all cells in a column are marked by the same player:

- **For the Human**:  
  \( \forall j \, (H(0, j) \land H(1, j) \land H(2, j)) \to W_H \)

- **For the Computer**:  
  \( \forall j \, (C(0, j) \land C(1, j) \land C(2, j)) \to W_C \)

#### Diagonals

A player wins if all cells in a diagonal are marked by the same player:

- **For the Human**:

  - Primary diagonal:  
    \( (H(0, 0) \land H(1, 1) \land H(2, 2)) \to W_H \)
  - Secondary diagonal:  
    \( (H(0, 2) \land H(1, 1) \land H(2, 0)) \to W_H \)

- **For the Computer**:
  - Primary diagonal:  
    \( (C(0, 0) \land C(1, 1) \land C(2, 2)) \to W_C \)
  - Secondary diagonal:  
    \( (C(0, 2) \land C(1, 1) \land C(2, 0)) \to W_C \)

---

### Draw Condition

If all cells are filled and no player has won, the game results in a draw:

\[
\neg W_H \land \neg W_C \to D
\]

Where:

- \( \neg W_H \): The human has not won.
- \( \neg W_C \): The computer has not won.

---

### Rules of Inference

#### Modus Ponens

If \( p \to q \) is true and \( p \) is true, then \( q \) must also be true.

**Example**:  
If:  
\( H(0, 0) \land H(0, 1) \land H(0, 2) \to W_H \)

And \( H(0, 0) \land H(0, 1) \land H(0, 2) \) is true,  
Then \( W_H \) (the human wins).

---

### Sample Playthrough

#### Initial Board

[ | | ]
[ | | ]
[ | | ]

#### The human plays X on 0 0 (The first row and first colomn)

[ X | | ]
[ | | ]
[ | | ]

#### The computer plays O on 1 1

[ X | | ]
[ | O | ]
[ | | ]

#### The human plays on 0 1

[ X | X | ]
[ | O | ]
[ | | ]

#### The computer plays on 2 2

[ X | X | ]
[ | O | ]
[ | | O ]

#### The Human plays on 0 2

[ X | X | X ]
[ | O | ]
[ | | O ]

So based on Modus Ponens, since
\( H(0, 0) \land H(0, 1) \land H(0, 2) \to W_H \)

And \( H(0, 0) \land H(0, 1) \land H(0, 2) \) is true,  
Then \( W_H \) (the human wins).
