
/*****************************************************************

	get Foreground Window title

	����ƒ��̃E�C���h�E�iForegroundWindow�j��
	�^�C�g����Ԃ�

	GetWindowText�d�l�A1024�����܂ŁB
	���v���Z�X���̓_�����ď����Ă������C�����邯��
	����ł����Ɠ����̂ł܂��ǂ��Ƃ��悤

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
