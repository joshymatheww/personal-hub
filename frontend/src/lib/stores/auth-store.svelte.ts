import type { UserProfile } from '$lib/types/auth';
import Cookies from 'js-cookie';

class AuthStore {
	token = $state<string | null>(Cookies.get('auth_token') || null);
	user = $state<UserProfile | null>(null);
	isLoadingUser = $state(false);

	isAuthenticated = $derived(this.token !== null);

	login(token: string) {
		this.token = token;
		Cookies.set('auth_token', token, {
			expires: 30 / (24 * 60),
			secure: true,
			sameSite: 'strict'
		});
	}

	setUser(userProfile: UserProfile) {
		this.user = userProfile;
		this.isLoadingUser = false;
	}

	logout() {
		this.user = null;
		this.token = null;

		Cookies.remove('auth_token');
	}
}

export const authStore = new AuthStore();
