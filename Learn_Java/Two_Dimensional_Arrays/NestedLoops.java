package Learn_Java.Two_Dimensional_Arrays;

public class NestedLoops {
	public static void main(String[] args) {
		int[] seatsDayOne = {850007, 841141, 150017, 622393, 178505, 952093, 492450, 790218, 515994, 926666, 476090, 709827, 908660, 718422, 641067, 624652, 429205, 394328, 802772, 468793, 901979, 504963, 733939, 706557, 724430, 663772, 577480, 886333, 323197, 283056, 378922, 628641, 494605, 606387, 179993, 755472, 253608, 975198, 328457, 885712, 411958, 418586, 254970, 299345, 632115, 915208, 661570, 328375, 538422, 321303};
    
		int[] seatsDayTwo = {740912, 209431, 310346, 316462, 915797, 850440, 803140, 459194, 293277, 302424, 790507, 711980, 639916, 707446, 940339, 613076, 524157, 189604, 595934, 509691, 234133, 787575, 674602, 944308, 710345, 889699, 622393, 151931, 964325, 944568, 357684, 933857, 541190, 935076, 468848, 449446, 278951, 885503, 539124, 278723, 998622, 846182, 394328, 914002, 803795, 851135, 828760, 504936, 504322, 648644};
		
		int matchCounter = 0;
		// Fix the outer loop header to iterate through the first array of seats
		for(int i = 0; i < seatsDayOne.length; i++) {

			// Fix the inner loop header to iterate through the second array of seats
			for(int j = 0; j < seatsDayTwo.length; j++) {

				// Replace 1==2 with conditional logic to check if an element in the first array matches an element in the second array
				if(seatsDayOne[i] == seatsDayTwo[j]) {
					matchCounter++;
					System.out.println("Contestant: " + seatsDayOne[i] + ", Seat Day One: " + i + ", Seat Day Two: " + j);
					break;
				}
			}
		}
		System.out.println("The total number of contestants reserving seats on both days was: " + matchCounter);
	}
}

