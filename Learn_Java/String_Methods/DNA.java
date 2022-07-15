package Learn_Java.String_Methods;

// This program determines if there is a protein in a strand of DNA

public class DNA {
    
    public static void main(String[] args){

        // -. .-.   .-. .-.   .
        //   \   \ /   \   \ /
        //  / \   \   / \   \
        // ~   `-~ `-`   `-~ `-

        // Un-comment the DNA sequence wanted to be tested for a protein
        String dna1 = "ATGCGATACGCTTGA";
        //String dna2 = "ATGCGATACGTGA";
        //String dna3 = "ATTAATATGTACTGA";

        String dna = dna1;

        // Testing
        //System.out.println(dna.length());

        // Find the start of the protein
        int start = dna.indexOf("ATG");
        //System.out.println("Start: "+start);
        
        // Find the end of the protein
        int stop = dna.indexOf("TGA");
        //System.out.println("Stop: "+stop);

        if (start != -1 && stop != -1 && (stop - start) % 3 == 0) {
            System.out.println("The DNA sequence "+dna+" contains the protein:");
            String protein = dna.substring(start, stop+3);
            System.out.println("Protein: "+protein);
        } else {
            System.out.println("No protein present.");
        }
    }
}
