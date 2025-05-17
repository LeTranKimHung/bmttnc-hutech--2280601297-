print("Nhập các dòng văn bản (Nhập 'Done' để kết thúc)")
lines =[]
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\nCác dòng đã nhập dau khi chuyển thành in hoa")
for line in lines:
    print(line.upper())