def compress_string(chars):
    if not chars:
        return 0

    write = 0
    read = 0

    while read < len(chars):
        current_char = chars[read]
        count = 0

        while read < len(chars) and chars[read] == current_char:
            read += 1
            count += 1

        chars[write] = current_char
        write += 1

        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write


user_input = input("Введіть рядок для стиснення (наприклад, aaabbbccc): ")
chars = list(user_input)

print(f"Оригінальний масив: {chars}")
print(f"Оригінальна довжина: {len(chars)}")

new_length = compress_string(chars)

print(f"Стиснутий масив: {chars[:new_length]}")
print(f"Стиснутий рядок: {''.join(chars[:new_length])}")
print(f"Нова довжина: {new_length}")
