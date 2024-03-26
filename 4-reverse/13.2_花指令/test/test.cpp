#include <stdio.h>
#include <windows.h>

int main(int argc, char* argv[])
{
	const char* str1 = "Message";
	const char* str2 = "Title";

	HMODULE u32dll = LoadLibraryA("user32.dll");
	DWORD MsgBoxAddr = (DWORD)GetProcAddress(u32dll, "MessageBoxA");

	__asm
	{
		push 0; //MB_OK
		lea ebx, str2;
		push [ebx];
		lea ebx, str1;
		push [ebx];
		push NULL;
		jz dest
		jnz dest
	}

	__asm __emit 0xe8

dest:
	__asm
	{
		mov eax, MsgBoxAddr;
		call eax;
	}

	return 0;
}