export interface LoginDetails {
	email: string;
	password: string;
}

export interface UserProfile {
	id: number;
	first_name: string;
	last_name?: string;
	email: string;
}

export interface TokenResponse {
	access_token: string;
	token_type: string;
}
