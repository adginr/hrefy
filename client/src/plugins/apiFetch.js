import { $fetch } from "ohmyfetch";
const config = { baseURL: "http://localhost:8000/api/v1/" };
export default $fetch.create(config);
