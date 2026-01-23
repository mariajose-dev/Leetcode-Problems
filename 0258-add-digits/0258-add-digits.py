class Solution(object):
    def addDigits(self, num):
        # Repeat until the number becomes a single digit
        while num >= 10:
            sum = 0  # stores sum of digits

            # Extract and add each digit of the number
            while num > 0:
                rem = num % 10      # get last digit
                sum = sum + rem     # add digit to sum
                num = num // 10     # remove last digit

            # replace num with sum of its digits
            num = sum

        # return the final single-digit result
        return num


        