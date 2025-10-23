vocab = [ "aya", "ye", "woo", "ma"]

def solution(babbling):
    count = 0

    for word in babbling:
        temp = word
        prev = ""
        valid = True

        # test each word in 'babbling'
        while temp:
            for sound in vocab:
                if temp.startswith(sound) and sound != prev:
                    temp = temp[len(sound):]
                    prev = sound
                    break

            # when for loop fails for all sounds
            else:
                valid = False
                break

        if valid: count += 1
    return count