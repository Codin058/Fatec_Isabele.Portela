#!/bin/bash
clear

echo "Lista de shell script"

clear

echo "Exercício 1"

while true
# while true = faz um loop infinito até algo dentro dele o fazer "quebrar" (break)

do
    read -p "Digite um número: " n1
    read -p "Digite mais um: " n2

    echo "O que deseja fazer?"
    read -p "Soma(1) . Subtrair(2) . Multiplicar(3) . Dividir(4)" x

    case $x in
        0)
            echo "encerrando o programa"
            break
            ;;
        1)
            soma=$(expr $n1 + $n2)
            echo $soma
            ;;
        2)
            subt=$(expr $n1 - $n2)
            echo $subt
            ;;
        3)
            mult=$(expr $n1 \* $n2)
            echo $mult
            ;;
        4)
            divi=$(expr $n1 / $n2)
            echo $divi
            ;;
        *)
            echo "Escolha uma opção válida"
            ;;
    esac
done


clear

echo "Exercício 2"

while true
do
    read -p "Escreva o nome de um arquvo que deseja deletar: " arq

    if [ -f "$arq" ]
    # -f = verifica se existe e se é um arquivo, evitando deletar diretórios

    then
        rm "$arq"
        # áspas = para caso o arquivo possua espaço

        echo "Pronto! Arquivo $arq deletado"
        break
    else
        echo "Arquivo não encontrado..."
    fi
done


clear

echo "Exercício 3"

while true
do
    read -p "Escreva o nome de um arquivo que deseja renomear: " arq
    read -p "Pode dar o caminho?: " cami

    if [ -f "$cami/$arq" ]

    then
        read -p "Arquivo encontrado! Deseja renomear para: " nome
        read -p "e para onde quer mover o arquivo?: " dest

        if [ -d "$dest" ]
        # -d = verifica se o diretório existe
        
        then
            mv "$cami/$arq" "$dest/$nome"

            echo "Pronto! Arquivo $arq renomeado para $nome"
            echo "e movido para $dest"
            break
        else
            echo "O arquivo de destino não foi encontrado..."
        fi
    else
        echo "Arquivo ou caminho não encontrado..."
    fi
done


clear

echo "Exercício 4"

while true
do
    read -p "Escreva o nome de um arquivo que deseja mover: " arq
    read -p "Pode dar o caminho?: " cami

    if [ -f "$cami/$arq" ]

    then
        read -p "Arquivo encontrado! Para onde quer mover o arquivo?: " dest

        if [ -d "$dest" ]
        then
            mv "$cami/$arq" "$dest"

            echo "Arquivo $arq movido para $dest"
            break
        else
            echo "O destino não foi encontrado..."
        fi
    else
        echo "Arquivo ou caminho não encontrado..."
    fi
done


clear

echo "Exercício 5"

while true
do
    read -p "Pesquise por um usuário: " user

    if grep -q "^$user:" /etc/passwd
    # grep = procura
    #  /etc/passwd = onde os usuários ficam

    then 
        echo "$user foi encontrado"
        break
    else
        echo "$user inexistente"

        read -p "encerra buscas? (S/N): " resp

        if [ "$resp" = "S" ]
        then
            echo "ok!"
            break
        fi
    fi
done


clear

echo "Exercício 6"

while true
do
    read -p "Pesquise por uma palavra ou frase: " palavra
    read -p "Em qual arquivo quer procurar?: " arq

    if [ -f "$arq" ]
    then
        if grep -i "$palavra" "$arq"
        # -i = ignora quais letras são minúsculas e quais são maiúsculas

        then 
            break
        else
            echo "nada encontrado nesse arquivo"

            read -p "encerra buscas? (S/N): " resp

            if [ "$resp" = "S" ]
            then
                echo "ok!"
                break
            fi
        fi
    else
        echo "$arq não foi encontrado"
    fi
done

clear

echo "Exercício 7"

echo "Informações do usuário logado"

echo $USER #comando do sistema que puxa o usuário logado no momento. whoami tem a mesma função
echo $HOME #comndo do sistema que puxa o diretório HOME do usuário logado no momento
du -sh $HOME # du = disc usage, significa disco em uso. -s = resumo do disco. -h = o tamanho dele (que é legível)


clear

echo "Exercício 8"

echo "Todos os usuário conectados"

who


clear

echo "Exercício 9"

while true
do
    read -p "Escreva o nome de um arquvo que deseja alterar as permissões: " arq

    if [ -f "$arq" ]
    then
        read -p "Que permissões deseja dar?: " perm

        chmod $perm $arq

        echo "Pronto! Arquivo $arq com as novas permissões"
        ls -l
        break
    else
        echo "Arquivo não encontrado..."

        read -p "encerra? (S/N): " resp

        if [ "$resp" = "S" ]
        then
            echo "ok!"
            break
        fi
    fi
done


clear

echo "Exercício 10"

echo "Todos os processos em execução:"

ps -ef 


clear

echo "Exercício 11"

while true
do
    read -p "Qual é o PID do processo que deseja encerrar?: " pid

    if ps -ef | grep -w $pid
    # precisa executar os processos antes de de buscar pelo PID

    then
        echo "processo encontrado! matando processo..."
        kill -9 $pid
    else
        echo "processo não encontrado"

        read -p "encerra? (S/N): " resp

        if [ "$resp" = "S" ]
        then
            echo "ok!"
            break
        fi
    fi    

done

