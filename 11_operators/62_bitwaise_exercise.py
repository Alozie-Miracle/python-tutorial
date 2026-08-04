"""
Write a function which accepts a "flag" argument.

The flag will correspond to audio processing algorithms.

For each flag that is set when the function is called, print an appropriate message

for example:

process_audio(Flags.L|Flags.S)

prints:

Making louder...

De-essing...

Use the bitwise & operator to do this.

Next, if you haven't already done this, refactor your program so that it makes use of 
a disctionary containing flags and their corresponding text. Use a loop together with
the dictionary to process the flags.

"""
    
    

class Flags:
    LOUDER = L = 1
    DENOISE = N = 2
    DEESS = S = 4
    NORMALIZE = O = 8
    REMOVECLICKS = R = 16
    
def printb(value):
    # print("{:08b}".format(value))
    print(f"{value:08b}")
    
    
def process_audio(flags):
    lookup = {
        Flags.LOUDER: "Making louder",
        Flags.DENOISE: "Removing noise",
        Flags.DEESS: "De-essing",
        Flags.NORMALIZE: "Normalizing",
        Flags.REMOVECLICKS: "Removing clicks"
    }
    
    for flag, description in lookup.items():
        if flag & flags:
            print(f"{description}...")
    

def main():
    combined_flags = Flags.L | Flags.S | Flags.R
    process_audio(combined_flags)



if __name__ == "__main__":
    main()