# Tic-Tac-Toe Game

Tic Tac Toe is a simple two-player game played on a 3x3 grid. Players take turns marking a square with either X or O, trying to align three of their marks in a row, column, or diagonal.

---

## Propositional Logic

The game mechanics are defined using propositions that represent each cell of the 3x3 TicTacToe grid:

### Propositions

- **H(i, j):** The human has played in cell (i, j).
- **C(i, j):** The computer has played in cell (i, j).
- **E(i, j):** The cell (i, j) is empty.
- **W<sub>H</sub>:** The human wins.
- **W<sub>C</sub>:** The computer wins.
- **D:** The game ends in a draw.

---

### Winning Conditions

#### Rows

A player wins if all cells in a row are marked by the same player:

- For the Human:  
  ∀ i (H(i, 0) ∧ H(i, 1) ∧ H(i, 2)) → W<sub>H</sub>

- For the Computer:  
  ∀ i (C(i, 0) ∧ C(i, 1) ∧ C(i, 2)) → W<sub>C</sub>

#### Columns

A player wins if all cells in a column are marked by the same player:

- For the Human:  
  ∀ j (H(0, j) ∧ H(1, j) ∧ H(2, j)) → W<sub>H</sub>

- For the Computer:  
  ∀ j (C(0, j) ∧ C(1, j) ∧ C(2, j)) → W<sub>C</sub>

#### Diagonals

A player wins if all cells in a diagonal are marked by the same player:

- **For the Human**:
  - Primary diagonal:  
    (H(0, 0) ∧ H(1, 1) ∧ H(2, 2)) → W<sub>H</sub>
  - Secondary diagonal:  
    (H(0, 2) ∧ H(1, 1) ∧ H(2, 0)) → W<sub>H</sub>

- **For the Computer**:
  - Primary diagonal:  
    (C(0, 0) ∧ C(1, 1) ∧ C(2, 2)) → W<sub>C</sub>
  - Secondary diagonal:  
    (C(0, 2) ∧ C(1, 1) ∧ C(2, 0)) → W<sub>C</sub>

---

### Draw Condition

If all cells are filled and no player has won, the game results in a draw:

¬W<sub>H</sub> ∧ ¬W<sub>C</sub> → D

Where:

- ¬W<sub>H</sub> means the human doesn't win.
- ¬W<sub>C</sub> means the computer doesn't win.

---

### Rules of Inference

#### Modus Ponens

If \( p → q \) is true and \( p \) is true, then \( q \) must also be true.

**Example**:  
If:  
H(0, 0) ∧ H(0, 1) ∧ H(0, 2) → W<sub>H</sub>  

And:  
H(0, 0) ∧ H(0, 1) ∧ H(0, 2) is true,  

Then:  
W<sub>H</sub> (the human wins).

---

#### Modus Tollens

If \( p → q \) is true and \( q \) is false, then \( p \) must also be false.

**Example**:  
If:  
\( C(0, 0) ∧ C(0, 1) ∧ E(0, 2) → W<sub>C</sub> \)  
And:  
\( ¬W<sub>C</sub> \) (the computer doesn't win),  

Then:  
\( E(0, 2) \) is false (the cell (0, 2) must be occupied, meaning the computer does not have a winning move).

---

#### Disjunctive Syllogism

If \( p ∨ q \) is true, and \( ¬p \) is true, then \( q \) must be true.

**Example**:  
If:  
The human can win in row 0 or row 1,  
And:  
\( ¬E(0, 2) \) (the human cannot play in that cell),  

Then:  
The human player must play in row 1 to be able to win.

---

#### Hypothetical Syllogism

If \( p → q \) and \( q → r \) are both true, then \( p → r \) is also true.

**Example**:  
If:  
Playing \( H(1, 1) \) makes winning possible,  
And:  
Winning at \( H(2, 2) \) is possible from that position,  

Then:  
Moving to \( H(1, 1) \) guarantees a potential win for the human player.


---

### Sample Playthrough

#### Initial Board

```
[   |   |   ]  
[   |   |   ]  
[   |   |   ]
```

#### The human plays X on (0,0) (The first row and first column)

```
[ X |   |   ]  
[   |   |   ]  
[   |   |   ]
```

#### The computer plays O on (1,1)

```
[ X |   |   ]
[   | O |   ]
[   |   |   ]
```

#### The human plays on (0,1)

```
[ X | X |   ]
[   | O |   ]
[   |   |   ]
```

#### The computer plays on (2, 2)

```
[ X | X |   ]
[   | O |   ]
[   |   | O ]
```

#### The Human plays on (0, 2)

```
[ X | X | X ]
[   | O |   ]
[   |   | O ]
```

So based on Modus Ponens, since
\( H(0, 0) \land H(0, 1) \land H(0, 2) \to W<sub>H</sub> \)

And \( H(0, 0) \land H(0, 1) \land H(0, 2) \) is true,  
Then \( W<sub>H</sub> \) (the human wins).
