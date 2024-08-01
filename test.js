function get_codes(codes){
    cod = []
    skip= ''
    code = ''
    for(i = 0;i<codes.length;i++){
        skip+= codes[i]
        if(codes[i] == ' ' ||codes[i] =='\n' ||  codes[i] =='' ){
            continue
        }
        code += codes[i]
        if(code.length == 16){
            cod.push(code)
            code = ''
        }
        if(code.length == 15 && (codes[skip.length] == '' || codes[skip.length] =='\n' || codes[skip.length] ==' ' ) ) {
            cod.push(code)
            console.log(skip)
            console.log(skip.length)
            code = ''
        }
    }

    return cod
}

codes = `
aaaa-aaaaaa-aaAc
aaaa-aaaaaa-aaAc
aaaa-aaaaaa-aaA
aaaa-aaaaaa-aaAa
aaaa-aaaaaa-aaAa
`

cod = get_codes(codes)
console.log(cod)


