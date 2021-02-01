
/*****************************************************************

	get Foreground Window title

	今作業中のウインドウ（ForegroundWindow）の
	タイトルを返す

	GetWindowText仕様、1024文字まで。
	他プロセス内はダメって書いてあった気もするけど
	これでちゃんと動くのでまあ良しとしよう

*****************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

	//GetWindowText GetForegroundWindow(),name,1024

main(){
	char	*name      = NULL ;

	name       = (char *)calloc( 1024+1, sizeof(char) );

	if ( GetWindowText(GetForegroundWindow(),name,1024) )
		printf("%s",name);

	free(name);
	exit(0);
}
