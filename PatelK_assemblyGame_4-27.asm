.data

test: .asciiz "You won a double! "
endGame: .asciiz "game ended"

Dice: .word 0, 0 #registers s0, s1 for the 2 dice
reRoll: .word 1, 1 #the dice that must be rerolled
rollNum: .word 1 #register t0

.text 

main:

loop: 
	jal RollDice #call RollDice function 
	move $s0, $a0 #move value from $v0 to $s0 for dice 1
	
	move $a0, $s0
	li $v0, 1
	syscall
	
	jal RollDice #call RollDice function 
	move $s1, $a0 #move value from $v0 to $s0 for dice 2
	
	move $a0, $s1
	li $v0, 1
	syscall
	
	#check for doubles 
	beq $s0, $s1, DoubleWon
	
	
	#when it is not a double 
	j end
	
################################################################################	
RollDice: #roll both die
	li $v0, 42 #range for random integer
	li $a1, 6 #set the range from 1 to 6  $t1
	li $a0, 1
	syscall
	
	
	jr $ra

################################################################################
DoubleWon: 
	li $v0, 4
	la $a0, test
	syscall
	
end: 
	li $v0, 4
	la $a0, endGame
	syscall