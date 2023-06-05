# Original
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# Minimize the number of print() function invocations by inserting the \n sequence into the strings
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

# Make the arrow twice as large (but keep the proportions)
print("     *       ")
print("    * *      ")
print("   *"," *    ",sep=2*" ")
print("  * ","  *   ",sep=2*" ")
print(" *  ","   *  ",sep=2*" ")
print("*** ","  *** ",sep=2*" ")
print("  * ","  *   ",sep=2*" ")
print("  * ","  *   ",sep=2*" ")
print("  **","***   ",sep=2*"*")

'''Duplicate the arrow, placing both arrows side by side; 
Note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring"
'''
print(2*"    *     ")       #<-- Add spaces after, otherwise the duplication will distort the arrow
print(2*"   * *    ")
print(2*"  *   *   ")
print(2*" *     *  ")
print(2*"***   *** ")
print(2*"  *   *   ")
print(2*"  *   *   ")
print(2*"  *****   ")