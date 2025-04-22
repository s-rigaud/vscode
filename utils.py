def sort_valid_words():
    # Sort valid word list
    with open("project-words.txt", encoding="utf-16") as f:
        words = f.read().splitlines()

    words.sort(key=lambda x: x.lower())

    with open("project-words.txt", "w", encoding="utf-16") as f:
        f.write("\n".join(words))

    print("Words sorted!")


def clean_ts_errors():
    # Clean TS error output
    with open("errors.txt", encoding="utf-8") as f:
        lines = f.read().splitlines()

    banned_errors = [
        "TS7005",  # "Parameter 'x' implicitly has an 'any' type."
        "TS7006",  # "Parameter 'x' implicitly has an 'any' type."
        "7034",  # "Variable 'x' implicitly has an 'any' type."
        "TS2304",  # "Cannot find name 'x'."
    ]

    banned_folders = ["build/"]

    accepted_lines = []
    for line in lines:
        for ban_word in banned_errors:
            if ban_word in line:
                break
        else:
            for ban_folder in banned_folders:
                if ban_folder in line:
                    break
            else:
                accepted_lines.append(line)

    with open("errors.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(accepted_lines))

    print("Errors cleaned!")


def get_files_most_errors():
    # Get files with most errors
    with open("spelling-errors.txt", encoding="utf-16") as f:
        lines = f.read().splitlines()

    file_errors = {}
    for line in lines:
        filename = line.split(":")[0]
        if filename not in file_errors:
            file_errors[filename] = 0

        file_errors[filename] += 1

    sorted_files = sorted(file_errors.items(), key=lambda x: x[1], reverse=True)

    with open("files_most_errors.txt", "w", encoding="utf-8") as f:
        for file, count in sorted_files:
            f.write(f"{file}: {count}\n")

    print("Files with most errors saved!")


def remove_misspelled_words():
    # Remove misspelled words from the list
    with open("project-words.txt", encoding="utf-16") as f:
        words = f.read().splitlines()

        misspelled_words = [
"Keybidings",
"keybindg",
"keybindining",
"knigh",
"knowledges",
"knwon"
        ]

    for word in misspelled_words:
        if word in words:
            words.remove(word)

    with open("project-words.txt", "w", encoding="utf-16") as f:
        f.write("\n".join(words))

    print("Misspelled words removed!")


sort_valid_words()
# clean_ts_errors()
# get_files_most_errors()
# remove_misspelled_words()
