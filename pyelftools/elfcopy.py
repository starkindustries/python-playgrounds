import sys

from elftools.elf.elffile import ELFFile


def inspect_elf(file, output):
    with open(file, "rb") as f, open(output, "wb") as outfile:
        elffile = ELFFile(f)

        print("elffile.header:", elffile.header)
        print("elffile.structs.Elf_Ehdr", elffile.structs.Elf_Ehdr)
        print("elffile.header.e_ehsize", elffile.header.e_ehsize)
        print("elffile.header.e_phoff:", elffile.header.e_phoff)
        print("elffile.header.e_phentsize:", elffile.header.e_phentsize)
        print("elffile.header.e_phnum:", elffile.header.e_phnum)
        print("elffile.header.e_shoff:", elffile.header.e_shoff)
        print("elffile.header.e_shentsize:", elffile.header.e_shentsize)
        print("elffile.headere_shnum:", elffile.header.e_shnum)
        print("elffile.e_ident_raw:", elffile.e_ident_raw)

        # Elf header
        f.seek(0)
        elf_header = f.read(elffile.header.e_ehsize)
        print("Writing elf header:", elf_header)
        outfile.write(elf_header)

        # Program header
        program_header_table_size = elffile.header.e_phentsize * elffile.header.e_phnum
        f.seek(elffile.header.e_ehsize, 0)
        program_header_table = f.read(program_header_table_size)
        print("Writing program header table:", program_header_table)
        outfile.seek(elffile.header.e_ehsize, 0)
        outfile.write(program_header_table)
        # files match up to 0x318 at this point

        # list all segments
        for segment in elffile.iter_segments():
            print("\nsegment.data", segment.data())
            print("segment.header.p_offset", segment.header.p_offset)
            print("segment.header.p_vaddr", segment.header.p_vaddr)
            print("segment.header.p_paddr", segment.header.p_paddr)
            print("segment.header.p_filesz", segment.header.p_filesz)
            print("segment.header.p_memsz", segment.header.p_memsz)
            print("segment.header.p_align", segment.header.p_align)
            print("Writing segment to file..")
            outfile.seek(segment.header.p_offset, 0)
            outfile.write(segment.data())

        # input("Press enter to continue..")

        # Section header table
        f.seek(elffile.header.e_shoff)
        section_header_table_size = elffile.header.e_shentsize * elffile.header.e_shnum
        section_header_table = f.read(section_header_table_size)
        print("Writing section header table:", section_header_table)
        outfile.seek(elffile.header.e_shoff, 0)
        outfile.write(section_header_table)
        # list all sections
        for section in elffile.iter_sections():
            print("\nsection.name:", section.name)
            print("section.data():", section.data())
            print("section.data_size:", section.data_size)
            print("section.data_alignment:", section.data_alignment)
            print("section.header.sh_link:", section.header.sh_link)
            print("section.header.sh_info:", section.header.sh_info)
            print(
                "section.header.sh_offset:",
                section.header.sh_offset,
                hex(section.header.sh_offset),
            )
            print(
                "section.header.sh_addr:",
                section.header.sh_addr,
                hex(section.header.sh_addr),
            )
            print("section:", section)
            print("section.structs:", section.structs)

            f.seek(section.header.sh_offset, 0)
            outfile.seek(section.header.sh_offset, 0)
            outfile.write(section.data())


if __name__ == "__main__":
    # // main.c
    # // compile with gcc main.c
    #  
    # #include <stdio.h>
    # int main()
    # {
    #     printf("Hello world!\n");
    # }

    if len(sys.argv) < 2:
        print("Usage: elfeditor.py <elf file>")
        sys.exit(1)
    file = sys.argv[1]
    inspect_elf(file, "output.bin")
